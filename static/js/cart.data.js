const handleTotalItemInCart = (response) => {
    const totalItemsInCart = response.total_items_in_cart;
    const totalItemsInCartContainer = document.getElementById("total-items-in-cart");
    const totalItemsInCartMobileContainer = document.getElementById("total-items-in-cart-mobile");
    totalItemsInCartContainer.textContent = totalItemsInCart;
    totalItemsInCartMobileContainer.textContent = totalItemsInCart;
}
const handleGrandTotal = (response) => {
    const totalGrandTotal = response.grand_total;
    const grandTotalContainer = document.getElementById("grand-total");
    const grandTotal = document.getElementById("grand-total-mobile");
    grandTotalContainer.textContent = totalGrandTotal;
    grandTotal.textContent = totalGrandTotal;
}


const getCartData = () => {
    const method = "GET";
    const xhr = new XMLHttpRequest();
    const responseType = "json";
    const request_url = "api/carts/";
    xhr.open(method, request_url, true);
    xhr.responseType = responseType;
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = () => {
        const response = xhr.response;
        console.log(response);
        if (xhr.status === 200) {
            handleTotalItemInCart(response);
            handleGrandTotal(response);
        }
    };
    xhr.send();
}

getCartData()