function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const addCart = {
    addProductCart(ProductID, Quantity) {
        return fetch(`${location.origin}/api/basket/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': ProductID,
                'quantity': Quantity
            })
        }).then(response => response.json()).then(data => {
            document.getElementById('cart-sidebar').innerHTML = '';
                for (let i in data) {
                            if (data[i]['product']['product']['in_sale'] == true) {
                                document.getElementById('cart-sidebar').innerHTML += `
                                <li class="item first">
                                    <div class="item-inner"><a class="product-image" title="${data[i]['product']['product']['name']}" href="{% url 'product_detail' pk=item.pk %}"><img alt="${data[i]['product']['product']['name']}" src="${data[i]['product']['cover_image']}"></a>
                                    <div class="product-details">
                                        <strong>${data[i]['quantity']}</strong> x <span class="price">${data[i]['product']['product']['new_price'].toFixed(2)}</span>
                                        <p class="product-name"><a href="{% url 'product_detail' pk=item.pk %}">${data[i]['product']['product']['name']}</a></p>
                                    </div>
                                    </div>
                                </li>`
                                document.getElementById('top-cart').style.display = 'block'
                            }
                            else {
                                document.getElementsByClassName('mini-products-list')[0].innerHTML += `
                                <li class="item first">
                                    <div class="item-inner"><a class="product-image" title="${data[i]['product']['product']['name']}" href="{% url 'product_detail' pk=item.pk %}"><img alt="${data[i]['product']['product']['name']}" src="${data[i]['product']['cover_image']}"></a>
                                    <div class="product-details">
                                        <strong>${data[i]['quantity']}</strong> x <span class="price">${data[i]['product']['product']['price'].toFixed(2)}</span>
                                        <p class="product-name"><a href="{% url 'product_detail' pk=item.pk %}">${data[i]['product']['product']['name']}</a></p>
                                    </div>
                                    </div>
                                </li>`
                                document.getElementById('top-cart').style.display = 'block'

                            }
                }
        })
    }
}

const addProduct = {
    addProductWishlist(ProductID) {
        return fetch(`${location.origin}/api/wishlist/`, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        }).then(response => response.json()).then(data => {
            if (data.success) {
                window.alert(data.message);
            }
        })
    }
}

const deleteProduct = {
    deleteProductWishlist(ProductID) {
        return fetch(`${location.origin}/api/wishlist`, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}

const deleteProduct_Basket = {
    deleteProductBasket(ProductID) {
        return fetch(`${location.origin}/api/basket/`, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product': ProductID
            })
        });
    }
}

function functionAddToWishlist(ProductID) {
    addProduct.addProductWishlist(ProductID);
}

function functionAddToBasket(ProductID) {
    const quantity = 1;
    addCart.addProductCart(ProductID, quantity);
}

function AddToBasketInDetail(ProductID) {
    const quantity = parseInt(document.getElementById('qty').value);
    addCart.addProductCart(ProductID, quantity);
}

function removeWishlist(ProductID) {
    deleteProduct.deleteProductWishlist(ProductID)
}

function removeBasket(ProductID) {
    deleteProduct_Basket.deleteProductBasket(ProductID)
}



let form = document.getElementById("newsletter-validate-detail")
form.addEventListener('submit', async function(event) {

    let postData = {
        email: form.email.value,
    }

    let response = await fetch(`${location.origin}/api/subscribers/`, {
        method: "POST",
        headers: {
                'X-CSRFToken': csrftoken,
                "Content-Type": "application/json"
        },
        body: JSON.stringify(postData)
    })
})