#!/usr/bin/env python3
"""
Main entry point for the application.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    """Main function to run the application."""
    print("Velkommen til dit Python-projekt!")
    print("Dette er entry point for din applikation.")
    
    # Example: Access environment variables
    debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
    if debug_mode:
        print("Debug mode er aktiveret")
    
    # Add your application logic here
    pass


if __name__ == "__main__":
    main()
