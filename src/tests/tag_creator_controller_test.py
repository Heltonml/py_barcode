from unittest.mock import patch
from src.libs.barcode_handler import BarcodeHandler
from src.controllers.tag_creator_controller import TagCreatorController

@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = 'image_path'
    mock_create_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()
    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert 'data' in result
    assert 'type' in result['data']
    assert 'count' in result['data']
    assert 'path' in result['data']

    assert result['data']['type'] == 'Tag Image.'
    assert result['data']['count'] == 1
    assert result['data']['path'] == f'{mock_value}.png'

def test_create_with_error():
    mock_value = 123456
    tag_creator_controller = TagCreatorController()

    try:
        tag_creator_controller.create(mock_value)
        assert False
    except Exception as exception:
        assert isinstance(exception, TypeError)
        assert exception.__class__.__name__ == 'TypeError'
