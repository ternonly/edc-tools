(async () => {
  const base64Data = 'BASE64_PLACEHOLDER';
  const selector = 'INPUT_SELECTOR_PLACEHOLDER';
  const fileName = 'FILENAME_PLACEHOLDER';
  const contentType = 'image/png';

  function base64ToBlob(base64, type) {
    const binStr = atob(base64);
    const len = binStr.length;
    const arr = new Uint8Array(len);
    for (let i = 0; i < len; i++) {
      arr[i] = binStr.charCodeAt(i);
    }
    return new Blob([arr], { type: type });
  }

  const blob = base64ToBlob(base64Data, contentType);
  const file = new File([blob], fileName, { type: contentType });
  const input = document.querySelector(selector);
  const dataTransfer = new DataTransfer();
  dataTransfer.items.add(file);
  input.files = dataTransfer.files;
  input.dispatchEvent(new Event('change', { bubbles: true }));
})();