from .download import download


def test_columns():
    df = download("ACIU", period="1mo")

    columns = df.columns.to_list()
    expected_columns = [
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Symbol",
    ]

    assert columns == expected_columns, "columns are not the same"
    assert len(df) > 0, "there should be at least one row"
    assert df["Symbol"].unique() == ["ACIU"], "symbol name should be added"
