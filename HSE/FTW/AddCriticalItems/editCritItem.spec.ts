import { test, expect } from '@playwright/test';

test('edit_critical_item', async ({ page }) => {
    test.setTimeout(120000); // 60 seconds timeout

    await page.goto('https://beats-stg.beraucoal.co.id/login');

    await page.getByPlaceholder('BeatsID').click();
    await page.getByPlaceholder('BeatsID').fill('XIIKM');
    await page.getByPlaceholder('Password').click();
    await page.getByPlaceholder('Password').fill('*!keykey');
    await page.getByRole('button', { name: ' Login' }).click();

    await page.locator('div').filter({ hasText: /^Administration$/ }).nth(1).click();
    await page.click('//*[@id="ROOT-2521314"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div/div[83]');

    await page.waitForTimeout(5000); // Wait for 5 seconds

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

    await page.waitForTimeout(5000); // Wait for 5 seconds

    await page.getByRole('gridcell', { name: 'Test' }).click();

    await page.getByRole('button', { name: 'Edit' }).click();
    await page.getByLabel('Nama Critical Items').click();
    await page.getByLabel('Nama Critical Items').fill('Test');
    await page.locator('label').click();
    await page.locator('label').click();
    await page.getByRole('button', { name: 'Simpan' }).click();
    
    await page.getByRole('gridcell', { name: 'Test' }).click();
    await page.click('//*[@id="ROOT-2521314"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div/div/div/div');
});
