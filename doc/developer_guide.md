# Developer Guide

## Getting Started

This guide will help you understand the structure and development process of the Custom PC Building module for Odoo 16 Community Edition.

## Module Structure

The module follows the MVC architecture and Odoo's code pattern. It consists of models, views, and controllers, each serving a specific purpose.

### Models

Models represent the data structure of the application. In this module, we have three models:

- `pc_components.py`: Represents the PC components with fields for component type, name, and specifications.
- `pc_builds.py`: Represents the PC builds with fields for the user, selected components, and build configuration.
- `saved_pc_builds.py`: Represents the user's saved PC builds with fields for the user, the build, and the timestamp of when the build was saved.

### Views

Views provide the user interface of the application. In this module, we have three views:

- `component_selection_view.xml`: Provides the interface for selecting PC components.
- `pc_build_preview_view.xml`: Provides the interface for previewing the PC build.
- `saved_pc_builds_view.xml`: Provides the interface for viewing the user's saved PC builds.

### Controllers

Controllers handle the logic of the application. In this module, we have three controllers:

- `component_selection_controller.py`: Handles the logic for component selection.
- `pc_build_preview_controller.py`: Handles the logic for PC build preview.
- `saved_pc_builds_controller.py`: Handles the logic for saved PC builds.

## Theme

The module uses a custom theme named "custom_pc_v7_nov_16". The CSS and JS files for the theme are located in the `static/css` and `static/js` directories respectively.

## Documentation

The module includes comprehensive documentation. The user guide (`user_guide.md`) provides instructions for using the module. The API documentation (`api_documentation.md`) provides information about the module's API.

## Development Process

The development process follows the best practices for Odoo module development. This includes writing clean, well-documented code, using version control, and thoroughly testing the module before deployment.

## Conclusion

The Custom PC Building module is a valuable feature for an ecommerce website. It allows users to customize a PC build, providing a unique selling proposition. The module is developed following the best practices for Odoo module development and includes comprehensive documentation.