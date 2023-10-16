use pyo3::prelude::*;

use unicode_bidi::BidiInfo;


#[pyfunction]
fn get_display(input: String) -> PyResult<String> {
    let bidi_info = BidiInfo::new(&input, None);

    Ok(bidi_info
        .paragraphs
        .iter()
        .map(|p| {
            bidi_info.reorder_line(p, p.range.clone())
        })
        .collect::<Vec<_>>()
        .join("\n"))
}


#[pymodule]
fn unicode_bidi_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_display, m)?)?;
    Ok(())
}