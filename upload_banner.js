(async () => {
  async function setFileFromUrl(selector, url, fileName) {
    const response = await fetch(url);
    const blob = await response.blob();
    const file = new File([blob], fileName, { type: blob.type });
    const input = document.querySelector(selector);
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    input.files = dataTransfer.files;
    input.dispatchEvent(new Event('change', { bubbles: true }));
  }

  // Banner
  await setFileFromUrl('input[aria-label="Add banner photo"]', 'https://sc02.alicdn.com/kf/A47e63e06446b4a8b8b5108abe2395441W.png', 'x-banner.png');
  // Wait a bit for the banner crop modal to appear
  await new Promise(r => setTimeout(r, 2000));
})();