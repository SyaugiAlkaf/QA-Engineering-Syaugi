import { test, expect } from '@playwright/test';

test('add_critical_item', async ({ page }) => {
  await page.goto('https://beats-stg.beraucoal.co.id/login');

  await page.getByPlaceholder('BeatsID').click();
  await page.getByPlaceholder('BeatsID').fill('XIIKM');
  await page.getByPlaceholder('Password').click();
  await page.getByPlaceholder('Password').fill('*!keykey');
  await page.getByRole('button', { name: ' Login' }).click();

  await page.locator('div').filter({ hasText: /^Administration$/ }).nth(1).click();
  await page.click('//*[@id="ROOT-2521314"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div[83]');

  // await page.getByRole('button', { name: 'Tambah' }).click();

  // await page.getByLabel('Nama Critical Items').click();
  // await page.getByLabel('Nama Critical Items').fill('Test');
  // await page.getByRole('button', { name: 'Simpan' }).click();

  const scrollableDivSelector = '.v-grid-scroller.v-grid-scroller-vertical';
  
  // Use Playwright's `scrollIntoView` for the element if applicable
  await page.locator(scrollableDivSelector).evaluate((element) => {
    element.scrollIntoView({ behavior: 'smooth', block: 'end' });
  });

  // Alternatively, use Playwright to drag the scroll thumb if needed
  const scrollableDiv = await page.$(scrollableDivSelector);
  if (scrollableDiv) {
    const box = await scrollableDiv.boundingBox();
    if (box) {
      // Simulate dragging the scroll thumb
      await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2);
      await page.mouse.down();
      await page.mouse.move(box.x + box.width / 2, box.y + box.height);
      await page.mouse.up();
    }
  }

  await page.getByRole('gridcell', { name: 'Test' }).click();
});
