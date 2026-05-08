(async () => {
  try {
    const imageUrl = 'https://sc02.alicdn.com/kf/Aa39a7c0da36d41a0bb804e497a56d1492.png';
    const response = await fetch(imageUrl);
    const blob = await response.blob();
    const file = new File([blob], 'water-purification.png', { type: 'image/png' });

    const input = document.querySelector('input[type="file"]');
    if (!input) {
      console.error('File input not found');
      return;
    }

    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    input.files = dataTransfer.files;

    input.dispatchEvent(new Event('change', { bubbles: true }));
    console.log('Image attached successfully');
  } catch (error) {
    console.error('Error attaching image:', error);
  }
})();
