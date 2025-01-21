document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".add-to-order");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const name = button.dataset.name;
            const price = button.dataset.price;

            let orderItems = JSON.parse(localStorage.getItem("orderItems")) || [];
            const existingItem = orderItems.find(item => item.name === name);

            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                orderItems.push({ name, price, quantity: 1 });
            }

            localStorage.setItem("orderItems", JSON.stringify(orderItems));
            alert(`Товар "${name}" добавлен в заказ!`);
            window.location.href = "/order/"; // Перенаправление на страницу заказа
        });
    });
});