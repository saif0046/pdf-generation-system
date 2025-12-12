import os
from src.core.random_generator import RandomDataGenerator
from src.infrastructure.storage import Storage

class PDFBatchGenerator:
    """
    Responsible for orchestrating the entire PDF generation cycle.
    Loads template, generates random values, replaces placeholders,
    and exports PDFs into the output folder.
    """

    def __init__(self, config, processor, logger):
        self.config = config
        self.processor = processor
        self.logger = logger

    def build_replacements(self):
        """
        Build a dictionary where each placeholder (e.g. {{name}})
        is mapped to a randomly generated value based on strategy.

        Returns:
            dict: {placeholder: random_value}
        """
        replacements = {}
        for placeholder, strategy in self.config["placeholders"].items():
            # Uses RandomDataGenerator to produce a correct value
            replacements[placeholder] = RandomDataGenerator.generate(strategy)
        return replacements

    def run(self):
        """
        Main workflow:
        - Ensures output directory exists
        - Loads the HTML template once
        - Generates random values 100 times (or configured count)
        - Replaces placeholders
        - Converts HTML to PDF for each iteration
        """
        output_dir = self.config["output_dir"]
        Storage.ensure_dir(output_dir)

        # Load HTML template ONCE for efficiency
        base_html = self.processor.get_document_html()

        # Load HTML template ONCE for efficiency
        for i in range(1, self.config["count"] + 1):
            self.logger.info(f"Generating PDF {i}/{self.config['count']}")

            # Create placeholder → random value mapping and Replace placeholders inside template
            replacements = self.build_replacements()
            filled_html = self.processor.replace_placeholders(base_html, replacements)

            # Create output path such as output_pdfs/document_001.pdf, Convert combined HTML - PDF
            output_path = os.path.join(output_dir, f"document_{i:03}.pdf")
            self.processor.html_to_pdf(filled_html, output_path)

            self.logger.info(f"Generated: {output_path}")
