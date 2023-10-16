use gtokenizers::tokenizers::traits::Tokenizer;
use pyo3::prelude::*;
use pyo3::types::PyList;

use std::collections::HashMap;
use std::path::Path;

use gtokenizers::models::region::Region;
use gtokenizers::models::region_set::RegionSet;
use gtokenizers::tokenizers::TreeTokenizer;

use crate::models::{PyRegion, PyTokenizedRegionSet, PyUniverse};

#[pyclass(name = "TreeTokenizer")]
pub struct PyTreeTokenizer {
    pub tokenizer: TreeTokenizer,
}

#[pymethods]
impl PyTreeTokenizer {
    #[new]
    pub fn new(path: String) -> Self {
        let path = Path::new(&path);
        let tokenizer = TreeTokenizer::from(path);

        PyTreeTokenizer { tokenizer }
    }

    #[getter]
    pub fn universe(&self) -> PyResult<PyUniverse> {
        let regions = self
            .tokenizer
            .universe
            .regions
            .iter()
            .map(|x| PyRegion::new(x.chr.clone(), x.start, x.end))
            .collect::<Vec<_>>();
        let region_to_id = self
            .tokenizer
            .universe
            .region_to_id
            .iter()
            .map(|(k, v)| (PyRegion::new(k.chr.clone(), k.start, k.end), v.to_owned()))
            .collect::<HashMap<_, _>>();
        let length = self.tokenizer.universe.len();
        Ok(PyUniverse {
            regions,
            region_to_id,
            length,
        })
    }

    pub fn __len__(&self) -> usize {
        self.tokenizer.universe.len() as usize
    }

    pub fn __repr__(&self) -> String {
        format!(
            "TreeTokenizer({} total regions)",
            self.tokenizer.universe.len()
        )
    }

    ///
    /// Tokenize a list of regions
    ///
    /// # Arguments
    /// - `regions` - a list of regions
    ///
    /// # Returns
    /// A PyTokenizedRegionSet that contains regions, bit_vector, and ids
    pub fn tokenize(&self, regions: &PyList) -> PyResult<PyTokenizedRegionSet> {
        // attempt to map the list to a vector of regions
        let regions = regions
            .iter()
            .map(|x| {
                // extract chr, start, end
                // this lets us interface any python object with chr, start, end attributes
                let chr = x.getattr("chr").unwrap().extract::<String>().unwrap();
                let start = x.getattr("start").unwrap().extract::<u32>().unwrap();
                let end = x.getattr("end").unwrap().extract::<u32>().unwrap();

                Region { chr, start, end }
            })
            .collect::<Vec<_>>();

        // create RegionSet
        let rs = RegionSet::from(regions);

        // tokenize
        let tokenized_regions = self.tokenizer.tokenize_region_set(&rs);

        // create pytokenizedregionset
        let tokenized_regions = match tokenized_regions {
            Some(tokenized_regions) => {
                let regions = tokenized_regions
                    .into_iter()
                    .map(|x| PyRegion::new(x.chr.clone(), x.start, x.end))
                    .collect::<Vec<_>>();
                let bit_vector = tokenized_regions.to_bit_vector();
                let ids = tokenized_regions.to_region_ids();
                Ok(PyTokenizedRegionSet::new(regions, bit_vector, ids))
            }
            // return error if tokenized_regions is None
            None => {
                return Err(pyo3::exceptions::PyValueError::new_err(
                    "Failed to tokenize regions",
                ))
            }
        };

        tokenized_regions
    }

    ///
    /// Encode a list of regions to a vector of ids
    ///
    /// # Arguments
    /// - `regions` - a list of regions
    ///
    /// # Returns
    /// A vector of ids
    pub fn encode_to_ids(&self, regions: &PyList) -> PyResult<Vec<u32>> {
        let res = self.tokenize(regions)?;
        Ok(res.ids)
    }

    ///
    /// Encode a list of regions to a bit vector
    ///
    /// # Arguments
    /// - `regions` - a list of regions
    ///
    /// # Returns
    /// A bit vector
    pub fn encode_to_bit_vector(&self, regions: &PyList) -> PyResult<Vec<bool>> {
        let res = self.tokenize(regions)?;
        Ok(res.bit_vector)
    }
}
