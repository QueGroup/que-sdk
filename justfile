#!/usr/bin/env just --justfile

# Show help message
help:
	@echo "🌟 Welcome to the Awesome Justfile! 🌟"
	@echo ""
	@echo "Available targets:"
	@echo "  - lint      : Run pre-commit 🐶"
	@echo "  - help      : Show this help message ℹ️"

# Run pre-commit lint
lint:
    @pre-commit run --all-files
