(async () => {
  const img = document.querySelector('img');
  if (!img) return { error: 'img not found' };
  const canvas = document.createElement('canvas');
  canvas.width = img.naturalWidth;
  canvas.height = img.naturalHeight;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0);
  return { base64: canvas.toDataURL('image/png').split(',')[1] };
})()