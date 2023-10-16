use roxmltree::Node;

use codec::{
    schema::{
        shortcuts::{em, p, q, s, section, strong, sub, sup, text, u},
        Article, AudioObject, AudioObjectOptions, Block, Blocks, Heading, ImageObject,
        ImageObjectOptions, Inline, Inlines, MediaObject, MediaObjectOptions, ThematicBreak,
    },
    Losses,
};

use super::utilities::{extend_path, record_attrs_lost, record_node_lost};

/// Decode the `<body>` of an `<article>`
///
/// Iterates over all child elements and either decodes them (by delegating to
/// the corresponding `decode_*` function for the element name), or adds them to
/// losses.
pub(super) fn decode_body(path: &str, node: &Node, article: &mut Article, losses: &mut Losses) {
    article.content = decode_blocks(path, node, losses, 0)
}

/// Decode block content nodes
///
/// Iterates over all child elements and either decodes them, or adds them to
/// losses.
fn decode_blocks(path: &str, node: &Node, losses: &mut Losses, depth: u8) -> Blocks {
    let mut blocks = Blocks::new();
    for child in node.children() {
        let tag = child.tag_name().name();
        let child_path = extend_path(path, tag);
        let block = match tag {
            "hr" => decode_hr(&child_path, &child, losses),
            "p" => decode_p(&child_path, &child, losses),
            "title" => decode_title(&child_path, &child, losses, depth),
            "sec" => decode_sec(&child_path, &child, losses, depth + 1),
            _ => {
                record_node_lost(path, &child, losses);
                continue;
            }
        };
        blocks.push(block);
    }
    blocks
}

/// Decode a `<hr>` to a [`Block::ThematicBreak`]
fn decode_hr(path: &str, node: &Node, losses: &mut Losses) -> Block {
    record_attrs_lost(path, node, [], losses);

    Block::ThematicBreak(ThematicBreak::new())
}

/// Decode a `<p>` to a [`Block::Paragraph`]
fn decode_p(path: &str, node: &Node, losses: &mut Losses) -> Block {
    record_attrs_lost(path, node, [], losses);

    p(decode_inlines(path, node, losses))
}

/// Decode a `<sec>` to a [`Block::Section`]
fn decode_sec(path: &str, node: &Node, losses: &mut Losses, depth: u8) -> Block {
    record_attrs_lost(path, node, [], losses);

    section(decode_blocks(path, node, losses, depth))
}

/// Decode a `<title>` to a [`Block::Heading`]
fn decode_title(path: &str, node: &Node, losses: &mut Losses, depth: u8) -> Block {
    record_attrs_lost(path, node, [], losses);

    Block::Heading(Heading::new(
        depth as i64,
        decode_inlines(path, node, losses),
    ))
}

/// Decode inline content nodes
///
/// Iterates over all child elements and either decodes them, or adds them to
/// losses.
fn decode_inlines(path: &str, node: &Node, losses: &mut Losses) -> Inlines {
    let mut inlines = Inlines::new();
    for child in node.children() {
        let inline = if child.is_text() {
            text(child.text().unwrap_or_default())
        } else {
            let tag = child.tag_name().name();
            let child_path = extend_path(path, tag);
            match tag {
                "inline-media" | "inline-graphic" => {
                    decode_inline_media(&child_path, &child, losses)
                }
                _ => {
                    record_attrs_lost(&child_path, &child, [], losses);

                    match tag {
                        "bold" => strong(decode_inlines(&child_path, &child, losses)),
                        "inline-quote" => q(decode_inlines(&child_path, &child, losses)),
                        "italic" => em(decode_inlines(&child_path, &child, losses)),
                        "strike" => s(decode_inlines(&child_path, &child, losses)),
                        "sub" => sub(decode_inlines(&child_path, &child, losses)),
                        "sup" => sup(decode_inlines(&child_path, &child, losses)),
                        "underline" => u(decode_inlines(&child_path, &child, losses)),
                        _ => {
                            record_node_lost(path, &child, losses);
                            continue;
                        }
                    }
                }
            }
        };
        inlines.push(inline);
    }
    inlines
}

/// Decode a `<inline-media>` to a [`Inline::AudioObject`], [`Inline::ImageObject`],
/// or [`Inline::VideoObject`]
///
/// Resolves the destination type based on the `mimetype` attribute of the element.
fn decode_inline_media(path: &str, node: &Node, losses: &mut Losses) -> Inline {
    let content_url = node.attribute("href").map(String::from).unwrap_or_default();

    let mime_type = node.attribute("mimetype").map(String::from);
    let mime_subtype = node.attribute("mime-subtype").map(String::from);
    let media_type = match (&mime_type, &mime_subtype) {
        (Some(r#type), Some(subtype)) => Some(format!("{type}/{subtype}")),
        (Some(r#type), None) => Some(r#type.clone()),
        _ => None,
    };

    record_attrs_lost(path, node, ["href", "mimetype", "mime-subtype"], losses);

    let mut alternate_names = None;
    let mut description = None;
    for child in node.children() {
        let tag = child.tag_name().name();
        match tag {
            "alt-text" => alternate_names = child.text().map(|content| vec![content.to_string()]),
            "long-desc" => description = child.text().map(|content| vec![p([text(content)])]),
            _ => record_node_lost(path, &child, losses),
        }
    }

    match mime_type.as_deref() {
        Some("audio") => Inline::AudioObject(AudioObject {
            content_url,
            media_type,
            options: Box::new(AudioObjectOptions {
                alternate_names,
                description,
                ..Default::default()
            }),
            ..Default::default()
        }),
        Some("inline") => Inline::ImageObject(ImageObject {
            content_url,
            media_type,
            options: Box::new(ImageObjectOptions {
                alternate_names,
                description,
                ..Default::default()
            }),
            ..Default::default()
        }),
        Some("video") => Inline::AudioObject(AudioObject {
            content_url,
            media_type,
            options: Box::new(AudioObjectOptions {
                alternate_names,
                description,
                ..Default::default()
            }),
            ..Default::default()
        }),
        _ => Inline::MediaObject(MediaObject {
            content_url,
            media_type,
            options: Box::new(MediaObjectOptions {
                alternate_names,
                description,
                ..Default::default()
            }),
            ..Default::default()
        }),
    }
}
