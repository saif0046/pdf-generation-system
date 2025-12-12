from src.core.orchestrator import PDFBatchGenerator
from src.core.template_processor import TemplateProcessor
from src.core.config_loader import ConfigLoader
from src.utils.logger import get_logger

def main():
    # Load configuration from the `config.json` file (returns a dict).
    # Expected keys: service_account_file, template_document_id, output_dir, count, placeholders, etc.
    config = ConfigLoader.load("config.json")

    # Create a logger named "PDF-GENERATOR".
    logger = get_logger("PDF-GENERATOR")


    # TemplateProcessor performs template loading, placeholder replacement, and PDF export.
    processor = TemplateProcessor(logger)

    # Create the orchestrator (PDFBatchGenerator) which coordinates the whole process.
    # It receives the config, the processor, and logger to run the job.
    orchestrator = PDFBatchGenerator(config, processor, logger)

    # Start the batch generation process (this will loop and create N PDFs as per config).
    orchestrator.run()


if __name__ == "__main__":
    main()
