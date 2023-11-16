# Custom PC Building Module API Documentation

## Overview

This document provides the API documentation for the Custom PC Building Module in Odoo 16 Community Edition.

## Models

### PC Components Model

- `GET /api/pc_components`: Returns a list of all PC components.
- `GET /api/pc_components/<id>`: Returns the details of a specific PC component.
- `POST /api/pc_components`: Creates a new PC component.
- `PUT /api/pc_components/<id>`: Updates a specific PC component.
- `DELETE /api/pc_components/<id>`: Deletes a specific PC component.

### PC Builds Model

- `GET /api/pc_builds`: Returns a list of all PC builds.
- `GET /api/pc_builds/<id>`: Returns the details of a specific PC build.
- `POST /api/pc_builds`: Creates a new PC build.
- `PUT /api/pc_builds/<id>`: Updates a specific PC build.
- `DELETE /api/pc_builds/<id>`: Deletes a specific PC build.

### Saved PC Builds Model

- `GET /api/saved_pc_builds`: Returns a list of all saved PC builds.
- `GET /api/saved_pc_builds/<id>`: Returns the details of a specific saved PC build.
- `POST /api/saved_pc_builds`: Saves a new PC build.
- `PUT /api/saved_pc_builds/<id>`: Updates a specific saved PC build.
- `DELETE /api/saved_pc_builds/<id>`: Deletes a specific saved PC build.

## Controllers

### Component Selection Controller

- `POST /api/component_selection`: Selects components for a PC build.
- `PUT /api/component_selection/<id>`: Updates the selected components for a specific PC build.

### PC Build Preview Controller

- `GET /api/pc_build_preview/<id>`: Previews a specific PC build.

### Saved PC Builds Controller

- `POST /api/saved_pc_builds`: Saves a PC build.
- `GET /api/saved_pc_builds/<id>`: Retrieves a specific saved PC build.
- `DELETE /api/saved_pc_builds/<id>`: Deletes a specific saved PC build.

## Error Handling

The API includes robust error handling. In case of an error, the API will return a JSON response with an `error` key, containing a message about what went wrong. For example:

```json
{
    "error": "Invalid input: The component does not exist."
}
```

## Conclusion

This API documentation provides the necessary details for interacting with the Custom PC Building Module. For more detailed information, please refer to the user guide and developer guide.