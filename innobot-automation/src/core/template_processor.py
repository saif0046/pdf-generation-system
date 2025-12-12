from xhtml2pdf import pisa

class TemplateProcessor:
    """
    Responsible for:
    - Loading HTML template
    - Replacing placeholders with dynamic values
    - Converting final HTML into PDF
    """
    def __init__(self, logger):
        self.logger = logger

    def get_document_html(self) -> str:
        """Load local HTML template with placeholders intact."""
        with open("template.html", "r", encoding="utf-8") as f:
            return f.read()

    def replace_placeholders(self, html: str, replacements: dict) -> str:
        """Replace placeholders inside the HTML string."""
        updated_html = html
        for placeholder, value in replacements.items():
            updated_html = updated_html.replace(placeholder, value)
        return updated_html

    def html_to_pdf(self, html: str, output_path: str):
        """Generate PDF using xhtml2pdf."""
        with open(output_path, "wb") as pdf_file:
            pisa.CreatePDF(
                src=html,
                dest=pdf_file
            )
