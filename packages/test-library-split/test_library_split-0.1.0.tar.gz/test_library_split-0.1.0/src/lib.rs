use pyo3::prelude::*;

#[pyfunction]
fn split_string(text: &str) -> Vec<String> {
    text.split_whitespace()
        .map(|token| token.to_string())
        .collect()
}

#[pymodule]
fn test_library_split(_python: Python, module: &PyModule) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(split_string, module)?)?;

    Ok(())
}
