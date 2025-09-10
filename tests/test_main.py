"""
Tests for main.py
"""

import pytest
from unittest.mock import patch
import main


def test_main_function_runs():
    """Test that main function runs without errors."""
    with patch('builtins.print') as mock_print:
        main.main()
        mock_print.assert_called()


def test_main_function_with_debug():
    """Test main function with debug mode enabled."""
    with patch('builtins.print') as mock_print, \
         patch('os.getenv', return_value='true'):
        main.main()
        mock_print.assert_called()


if __name__ == "__main__":
    pytest.main([__file__])
