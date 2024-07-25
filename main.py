from pdf_processor import PDFProcessor

if __name__ == "__main__":
    config_path = "conf.json"  # Replace with your config file path
    pdf_processor = PDFProcessor(config_path)
    pdf_processor.process_all_pdfs()
    # pdf_processor.rename_logic()
