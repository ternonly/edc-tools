(async () => {
  try {
    const response = await fetch('https://sc02.alicdn.com/kf/A293ed1100fe1460dbe9b683117234889R.png');
    const buffer = await response.arrayBuffer();
    const file = new File([buffer], 'survival.png', { type: 'image/png' });
    const dt = new DataTransfer();
    dt.items.add(file);
    const input = document.querySelector('input[type="file"]');
    if (input) {
      input.files = dt.files;
      input.dispatchEvent(new Event('change', { bubbles: true }));
      console.log('UPLOAD_SUCCESS');
    } else {
      console.log('INPUT_NOT_FOUND');
    }
  } catch (e) {
    console.error(e);
  }
})();