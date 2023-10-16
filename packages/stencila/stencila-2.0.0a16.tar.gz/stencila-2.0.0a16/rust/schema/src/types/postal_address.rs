// Generated file; do not edit. See `schema-gen` crate.

use crate::prelude::*;

use super::block::Block;
use super::image_object_or_string::ImageObjectOrString;
use super::property_value_or_string::PropertyValueOrString;
use super::string::String;

/// A physical mailing address.
#[skip_serializing_none]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, ReadNode, WriteNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
#[jats(elem = "address")]
pub struct PostalAddress {
    /// The type of this item
    pub r#type: MustBe!("PostalAddress"),

    /// The identifier for this item
    #[strip(id)]
    #[html(attr = "id")]
    pub id: Option<String>,

    /// Email address for correspondence.
    pub emails: Option<Vec<String>>,

    /// Telephone numbers for the contact point.
    pub telephone_numbers: Option<Vec<String>>,

    /// The street address.
    pub street_address: Option<String>,

    /// The locality in which the street address is, and which is in the region.
    pub address_locality: Option<String>,

    /// The region in which the locality is, and which is in the country.
    pub address_region: Option<String>,

    /// The postal code.
    pub postal_code: Option<String>,

    /// The country.
    pub address_country: Option<String>,

    /// Non-core optional fields
    #[serde(flatten)]
    #[html(flatten)]
    #[jats(flatten)]
    #[markdown(flatten)]
    pub options: Box<PostalAddressOptions>,
}

#[skip_serializing_none]
#[derive(Debug, SmartDefault, Clone, PartialEq, Serialize, Deserialize, StripNode, HtmlCodec, JatsCodec, MarkdownCodec, TextCodec, ReadNode, WriteNode)]
#[serde(rename_all = "camelCase", crate = "common::serde")]
pub struct PostalAddressOptions {
    /// Alternate names (aliases) for the item.
    pub alternate_names: Option<Vec<String>>,

    /// A description of the item.
    #[strip(types)]
    pub description: Option<Vec<Block>>,

    /// Any kind of identifier for any kind of Thing.
    pub identifiers: Option<Vec<PropertyValueOrString>>,

    /// Images of the item.
    pub images: Option<Vec<ImageObjectOrString>>,

    /// The name of the item.
    pub name: Option<String>,

    /// The URL of the item.
    pub url: Option<String>,

    /// Languages (human not programming) in which it is possible to communicate
    /// with the organization/department etc.
    pub available_languages: Option<Vec<String>>,

    /// The post office box number.
    pub post_office_box_number: Option<String>,
}

impl PostalAddress {
    pub fn new() -> Self {
        Self {
            ..Default::default()
        }
    }
}
