from pathlib import Path

from fpdf import FPDF
from test.utilities import assert_pdf_equal

HERE = Path(__file__).resolve().parent


class TestBarcodes:
    def test_code39(self, tmp_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.code39("fpdf2", x=50, y=50, w=4, h=20)
        pdf.set_font("courier", "B", size=36)
        pdf.text(x=80, y=80, txt="fpdf2")
        assert_pdf_equal(pdf, HERE / "barcodes_code39.pdf", tmp_path)

    def test_interleaved2of5(self, tmp_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.interleaved2of5("1337", x=65, y=50, w=4, h=20)
        pdf.set_font("courier", "B", size=36)
        pdf.text(x=80, y=80, txt="1337")
        assert_pdf_equal(pdf, HERE / "barcodes_interleaved2of5.pdf", tmp_path)
