document.addEventListener("DOMContentLoaded", () => {
    const itemsList = document.getElementById("order-items");
    const itemsField = document.getElementById("id_items");
    const quantitiesField = document.getElementById("id_quantities");

    // Получаем товары из LocalStorage
    let orderItems = JSON.parse(localStorage.getItem("orderItems")) || [];

    if (orderItems.length > 0) {
        itemsList.innerHTML = ""; // Очищаем список перед добавлением
        orderItems.forEach((item, index) => {
            const listItem = document.createElement("li");

            // Создаем поля для редактирования количества
            listItem.innerHTML = `${item.name} - ${item.price} руб. 
                <input type="number" value="${item.quantity}" min="1" 
                data-index="${index}" class="quantity-input" /> шт.`;

            itemsList.appendChild(listItem);
        });

        // Заполняем скрытые поля для отправки
        const items = orderItems.map(item => `${item.name} (${item.price} руб.)`).join(", ");
        const quantities = orderItems.map(item => item.quantity).join(", ");
        itemsField.value = items;
        quantitiesField.value = quantities;
    }

    // Обработчик изменения количества товара
    document.querySelectorAll(".quantity-input").forEach(input => {
        input.addEventListener("input", (e) => {
            const index = e.target.dataset.index;
            const newQuantity = parseInt(e.target.value, 10);

            if (newQuantity > 0) {
                orderItems[index].quantity = newQuantity;
                localStorage.setItem("orderItems", JSON.stringify(orderItems));

                // Обновляем скрытые поля
                const items = orderItems.map(item => `${item.name} (${item.price} руб.)`).join(", ");
                const quantities = orderItems.map(item => item.quantity).join(", ");
                itemsField.value = items;
                quantitiesField.value = quantities;
            }
        });
    });
});

document.querySelector("form").addEventListener("submit", () => {
    localStorage.removeItem("orderItems");
});