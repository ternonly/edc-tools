(async () => {
  try {
    const url = 'https://sc02.alicdn.com/kf/Addfe38a981b84f00968b3caa8a3604224.png';
    const response = await fetch(url);
    const blob = await response.blob();
    const file = new File([blob], 'avatar.png', { type: 'image/png' });
    
    // Find the hidden file input
    let input = document.querySelector('input[type="file"]');
    if (!input) {
      // Try to trigger the change avatar dialog to make sure input is there
      const buttons = Array.from(document.querySelectorAll('button'));
      const changeBtn = buttons.find(b => b.textContent.includes('更换头像') || b.textContent.includes('Change profile photo'));
      if (changeBtn) changeBtn.click();
      await new Promise(r => setTimeout(r, 1000));
      input = document.querySelector('input[type="file"]');
    }
    
    if (!input) return { __result: "Input not found" };
    
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    input.files = dataTransfer.files;
    input.dispatchEvent(new Event('change', { bubbles: true }));
    
    return { __result: "Injected and change event dispatched" };
  } catch (e) {
    return { __result: "Error: " + e.message };
  }
})();