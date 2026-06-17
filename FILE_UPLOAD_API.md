# File Upload API Documentation

## Overview
This API endpoint allows you to upload files to the server with proper authentication and metadata.

## Base Url
```
http://138.68.190.213:42069
```

## Endpoint
```
POST {base_url}/upload
```

## Authentication
The API requires two authentication methods:
- **Bearer Token**: Passed in the Authorization header
- **API Key**: Passed in the x-api-key header

## Request Format

### Headers
| Header | Value | Required | Description |
|--------|-------|----------|-------------|
| `Authorization` | `Bearer {token}` | Yes | User authentication token |
| `x-api-key` | `{USER_SERVICE_API_KEY}` | Yes | API key for service authentication |
| `x-device-id` | `string` | Yes | Unique device identifier |
| `user-agent` | `string` | Yes | Client user agent string |

### Request Body
The request uses `multipart/form-data` encoding with the following fields:

**Files:**
- `file`: The file to upload (binary data)
  - Filename: Original filename from the file path
  - Content: File binary content
  - MIME Type: Appropriate MIME type for the file

**Data:**
- `mediaType`: The type of media being uploaded (e.g., "image", "video", "document")

### Python Example
```python
import requests

# Prepare the file
file_path = Path("/path/to/file.ext")
mime_type = "application/javascript"
media_type = "script"

with open(file_path, 'rb') as f:
    files = {
        "file": (file_path.name, f, mime_type)
    }
    data = {
        "mediaType": media_type
    }
    upload_headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {token}",
        "x-api-key": USER_SERVICE_API_KEY,
        "x-device-id": "1"
    }
    
    response = requests.post(url, files=files, data=data, headers=upload_headers)
```

## Response Format

### Success Response
**HTTP Status Code:** `200 OK`

**Response Body:**
```json
{
  "success": true,
  "url": "http://138.68.190.213:42069/files/aaf5cea1-35c7-4a2a-b958-d579be272472.cjs",
  "filename": "aaf5cea1-35c7-4a2a-b958-d579be272472.cjs",
  "originalName": "drip-emporium.umd.cjs",
  "size": 325822,
  "mimeType": "application/javascript"
}
```

### Response Fields
| Field | Type | Description |
|-------|------|-------------|
| `success` | boolean | Indicates whether the upload was successful |
| `url` | string | Full URL where the uploaded file can be accessed |
| `filename` | string | Server-generated filename (UUID-based) |
| `originalName` | string | Original filename from the upload |
| `size` | integer | File size in bytes |
| `mimeType` | string | MIME type of the uploaded file |

## Error Responses

### 401 Unauthorized
Invalid or missing authentication credentials.

### 400 Bad Request
Invalid request format or missing required fields.

### 413 Payload Too Large
File size exceeds the maximum allowed limit.

## Notes
- Files are renamed on the server using UUID-based naming to prevent conflicts
- The original filename is preserved in the response for reference
- Ensure the MIME type matches the actual file type for proper handling
- The device ID should be consistent for the same device across requests
