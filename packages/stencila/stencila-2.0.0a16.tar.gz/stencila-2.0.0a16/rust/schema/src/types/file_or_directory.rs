// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::directory::Directory;
use super::file::File;

/// [`File`] or [`Directory`]
#[derive(Debug, Display, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, ReadNode, WriteNode)]
#[serde(untagged, crate = "common::serde")]
pub enum FileOrDirectory {
    File(File),

    Directory(Directory),
}
