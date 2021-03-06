from pathlib import Path

import fpdf
from test.utilities import assert_pdf_equal


HERE = Path(__file__).resolve().parent


def next_row(pdf):
    pdf.ln()
    pdf.set_y(pdf.get_y() + size + margin)


size = 50
margin = 10


class TestEllipse:
    def test_ellipse_not_circle(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        for counter, style in enumerate(["", "F", "FD", "DF", None]):
            pdf.ellipse(x=pdf.get_x(), y=pdf.get_y(), w=size / 2, h=size, style=style)
            pdf.set_x(pdf.get_x() + (size / 2) + margin)
            if counter % 3 == 0:
                next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_ellipse_not_circle.pdf", tmp_path)

    def test_ellipse_style(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        for counter, style in enumerate(["", "F", "FD", "DF", None]):
            pdf.ellipse(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=style)
            pdf.set_x(pdf.get_x() + size + margin)
            if counter % 3 == 0:
                next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_ellipse_style.pdf", tmp_path)

    def test_ellipse_line_width(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        for line_width in [1, 2, 3]:
            pdf.set_line_width(line_width)
            pdf.ellipse(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=None)
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)
        for line_width in [4, 5, 6]:
            pdf.set_line_width(line_width)
            pdf.ellipse(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=None)
            pdf.set_x(pdf.get_x() + size + margin)
        pdf.set_line_width(0.2)  # reset

        assert_pdf_equal(pdf, HERE / "class_ellipse_line_width.pdf", tmp_path)

    def test_ellipse_draw_color(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        pdf.set_line_width(0.5)
        for gray in [70, 140, 210]:
            pdf.set_draw_color(gray)
            pdf.ellipse(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=None)
            pdf.set_x(pdf.get_x() + size + margin)

        assert_pdf_equal(pdf, HERE / "class_ellipse_draw_color.pdf", tmp_path)

    def test_ellipse_fill_color(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        pdf.set_fill_color(240)
        for color in [[230, 30, 180], [30, 180, 30], [30, 30, 70]]:
            pdf.set_draw_color(*color)
            pdf.ellipse(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style="FD")
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_ellipse_fill_color.pdf", tmp_path)


class TestRectangle:
    def test_rect_not_square(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        for counter, style in enumerate(["", "F", "FD", "DF", None]):
            pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=size / 2, h=size, style=style)
            pdf.set_x(pdf.get_x() + (size / 2) + margin)
            if counter % 3 == 0:
                next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_rect_not_square.pdf", tmp_path)

    def test_rect_style(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        for counter, style in enumerate(["", "F", "FD", "DF", None]):
            pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=style)
            pdf.set_x(pdf.get_x() + size + margin)
            if counter % 3 == 0:
                next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_rect_style.pdf", tmp_path)

    def test_rect_line_width(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        for line_width in [1, 2, 3]:
            pdf.set_line_width(line_width)
            pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=None)
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)
        for line_width in [4, 5, 6]:
            pdf.set_line_width(line_width)
            pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=None)
            pdf.set_x(pdf.get_x() + size + margin)
        pdf.set_line_width(0.2)  # reset

        assert_pdf_equal(pdf, HERE / "class_rect_line_width.pdf", tmp_path)

    def test_rect_draw_color(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        # Colors
        pdf.set_line_width(0.5)
        for gray in [70, 140, 210]:
            pdf.set_draw_color(gray)
            pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style=None)
            pdf.set_x(pdf.get_x() + size + margin)

        assert_pdf_equal(pdf, HERE / "class_rect_draw_color.pdf", tmp_path)

    def test_rect_fill_color(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        pdf.set_fill_color(240)
        for color in [[230, 30, 180], [30, 180, 30], [30, 30, 70]]:
            pdf.set_draw_color(*color)
            pdf.rect(x=pdf.get_x(), y=pdf.get_y(), w=size, h=size, style="FD")
            pdf.set_x(pdf.get_x() + size + margin)

        next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_rect_fill_color.pdf", tmp_path)


class TestLine:
    def test_line(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        def draw_diagonal_line(pdf, x, y):
            pdf.line(x, y, x + size, y + size / 2)

        for width in [0.71, 1, 2]:
            pdf.set_line_width(width)
            draw_diagonal_line(pdf, pdf.get_x(), pdf.get_y())
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)

        for color in [70, 140, 200]:
            pdf.set_draw_color(color)
            draw_diagonal_line(pdf, pdf.get_x(), pdf.get_y())
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)

        assert_pdf_equal(pdf, HERE / "class_line.pdf", tmp_path)

    def test_dash(self, tmp_path):
        pdf = fpdf.FPDF(unit="mm")
        pdf.add_page()

        def draw_diagonal_dash(pdf, x, y, *a, **k):
            pdf.dashed_line(x, y, x + size, y + size / 2, *a, **k)

        for width in [0.71, 1, 2]:
            pdf.set_line_width(width)
            draw_diagonal_dash(pdf, pdf.get_x(), pdf.get_y(), margin, margin / 2)
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)

        for color in [70, 140, 200]:
            pdf.set_draw_color(color)
            draw_diagonal_dash(pdf, pdf.get_x(), pdf.get_y(), margin, margin / 2)
            pdf.set_x(pdf.get_x() + size + margin)
        next_row(pdf)

        pdf.set_draw_color(0)
        pdf.set_line_width(0.2)
        draw_diagonal_dash(pdf, pdf.get_x(), pdf.get_y(), margin, margin)

        pdf.set_x(pdf.get_x() + size + margin)
        draw_diagonal_dash(pdf, pdf.get_x(), pdf.get_y(), margin / 2, margin)

        next_row(pdf)
        pdf.set_line_width(1)
        x, y = pdf.get_x(), pdf.get_y()
        pdf.dashed_line(x, y, x + 100, y + 80, 10, 3)
        pdf.set_x(pdf.get_x() + 20)
        x, y = pdf.get_x(), pdf.get_y()
        pdf.dashed_line(x, y, x + 100, y + 80, 3, 20)
        pdf.set_x(pdf.get_x() + 20)
        x, y = pdf.get_x(), pdf.get_y()
        pdf.dashed_line(x, y, x + 100, y + 80, 6, 17)

        assert_pdf_equal(pdf, HERE / "class_dash.pdf", tmp_path)
