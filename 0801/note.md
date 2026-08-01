| Expected Condition                 | 等待條件          | 成功時回傳        | 常見用途                  |
|------------------------------------| ------------- | ------------ | --------------------- |
| `presence_of_element_located(locator)` | 元素已存在 DOM     | `WebElement` | 元素不一定看得到，只要 HTML 中存在  |
| `visibility_of_element_located(locator)` | 元素存在且可見       | `WebElement` | 等待輸入框、文字或圖片顯示         |
| `visibility_of(element)`           | 已取得的元素變成可見    | `WebElement` | 已先取得 `WebElement`     |
| `invisibility_of_element_located(locator)` | 元素消失或不可見      | `True` 或元素   | 等待 loading、遮罩、提示框消失   |
| `invisibility_of_element(element)` | 指定元素消失或不可見    | `True` 或元素   | 已經取得元素物件              |
