// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::block::Block;
use super::comment::Comment;
use super::creative_work_type::CreativeWorkType;
use super::creative_work_type_or_string::CreativeWorkTypeOrString;
use super::date::Date;
use super::grant_or_monetary_grant::GrantOrMonetaryGrant;
use super::image_object_or_string::ImageObjectOrString;
use super::inline::Inline;
use super::number::Number;
use super::person::Person;
use super::person_or_organization::PersonOrOrganization;
use super::person_or_organization_or_software_application::PersonOrOrganizationOrSoftwareApplication;
use super::property_value_or_string::PropertyValueOrString;
use super::string::String;
use super::string_or_number::StringOrNumber;
use super::thing_type::ThingType;

/// An audio file
#[skip_serializing_none]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, ReadNode, WriteNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
#[cfg_attr(feature = "proptest", derive(Arbitrary))]
#[html(elem = "audio", custom)]
#[jats(elem = "inline-media", special)]
#[markdown(format = "![]({content_url})")]
pub struct AudioObject {
    /// The type of this item
    #[cfg_attr(feature = "proptest", proptest(value = "Default::default()"))]
    pub r#type: MustBe!("AudioObject"),

    /// The identifier for this item
    #[strip(id)]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    #[html(attr = "id")]
    pub id: Option<String>,

    /// URL for the actual bytes of the media object, for example the image file or video file.
    #[cfg_attr(feature = "proptest-min", proptest(value = r#"String::from("https://example.org/image.png")"#))]
    #[cfg_attr(feature = "proptest-low", proptest(regex = r#"https://\w+\.\w+/\w+\.png"#))]
    #[cfg_attr(feature = "proptest-high", proptest(regex = r#"[a-zA-Z0-9]{1,100}"#))]
    #[cfg_attr(feature = "proptest-max", proptest(strategy = r#"String::arbitrary()"#))]
    #[html(attr = "src")]
    pub content_url: String,

    /// IANA media type (MIME type).
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub media_type: Option<String>,

    /// Non-core optional fields
    #[serde(flatten)]
    #[html(flatten)]
    #[jats(flatten)]
    #[markdown(flatten)]
    pub options: Box<AudioObjectOptions>,
}

#[skip_serializing_none]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, ReadNode, WriteNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
#[cfg_attr(feature = "proptest", derive(Arbitrary))]
pub struct AudioObjectOptions {
    /// Alternate names (aliases) for the item.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub alternate_names: Option<Vec<String>>,

    /// A description of the item.
    #[strip(types)]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub description: Option<Vec<Block>>,

    /// Any kind of identifier for any kind of Thing.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub identifiers: Option<Vec<PropertyValueOrString>>,

    /// Images of the item.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub images: Option<Vec<ImageObjectOrString>>,

    /// The name of the item.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub name: Option<String>,

    /// The URL of the item.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub url: Option<String>,

    /// The subject matter of the content.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub about: Option<Vec<ThingType>>,

    /// The authors of the `CreativeWork`.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub authors: Option<Vec<PersonOrOrganization>>,

    /// A secondary contributor to the `CreativeWork`.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub contributors: Option<Vec<PersonOrOrganizationOrSoftwareApplication>>,

    /// People who edited the `CreativeWork`.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub editors: Option<Vec<Person>>,

    /// The maintainers of the `CreativeWork`.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub maintainers: Option<Vec<PersonOrOrganization>>,

    /// Comments about this creative work.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub comments: Option<Vec<Comment>>,

    /// Date/time of creation.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub date_created: Option<Date>,

    /// Date/time that work was received.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub date_received: Option<Date>,

    /// Date/time of acceptance.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub date_accepted: Option<Date>,

    /// Date/time of most recent modification.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub date_modified: Option<Date>,

    /// Date of first publication.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub date_published: Option<Date>,

    /// People or organizations that funded the `CreativeWork`.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub funders: Option<Vec<PersonOrOrganization>>,

    /// Grants that funded the `CreativeWork`; reverse of `fundedItems`.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub funded_by: Option<Vec<GrantOrMonetaryGrant>>,

    /// Genre of the creative work, broadcast channel or group.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub genre: Option<Vec<String>>,

    /// Keywords or tags used to describe this content.
    /// Multiple entries in a keywords list are typically delimited by commas.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub keywords: Option<Vec<String>>,

    /// An item or other CreativeWork that this CreativeWork is a part of.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub is_part_of: Option<CreativeWorkType>,

    /// License documents that applies to this content, typically indicated by URL.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub licenses: Option<Vec<CreativeWorkTypeOrString>>,

    /// Elements of the collection which can be a variety of different elements,
    /// such as Articles, Datatables, Tables and more.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub parts: Option<Vec<CreativeWorkType>>,

    /// A publisher of the CreativeWork.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub publisher: Option<PersonOrOrganization>,

    /// References to other creative works, such as another publication,
    /// web page, scholarly article, etc.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub references: Option<Vec<CreativeWorkTypeOrString>>,

    /// The textual content of this creative work.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub text: Option<String>,

    /// The title of the creative work.
    #[strip(types)]
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub title: Option<Vec<Inline>>,

    /// The version of the creative work.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub version: Option<StringOrNumber>,

    /// Bitrate in megabits per second (Mbit/s, Mb/s, Mbps).
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub bitrate: Option<Number>,

    /// File size in megabits (Mbit, Mb).
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub content_size: Option<Number>,

    /// URL that can be used to embed the media on a web page via a specific media player.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub embed_url: Option<String>,

    /// The caption for this audio recording.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    #[html(attr = "alt")]
    pub caption: Option<String>,

    /// The transcript of this audio recording.
    #[cfg_attr(feature = "proptest", proptest(value = "None"))]
    pub transcript: Option<String>,
}

impl AudioObject {
    pub fn new(content_url: String) -> Self {
        Self {
            content_url,
            ..Default::default()
        }
    }
}
