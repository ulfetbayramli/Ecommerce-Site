const categoryFilter = {
  url: `${location.origin}/api/product_versions/`,

  filterProduct(categoryId) {
    let url = this.url;
    if (categoryId) {
      url += `?product__category=${categoryId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {
          for (let x in data[i]['product'].category) {
          if (data[i]['product']['category'][x] == categoryId || data[i]['product']['p_category'] == categoryId) {
            if (data[i]['product']['in_sale'] == true) {
              document.getElementById('products-list').innerHTML += `
                <li class="item first">
                  <div class="product-image"> <a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
                  <div class="product-shop">
                    <h2 class="product-name"><a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                    <div class="desc std">
                      <p>${data[i]['product']['overview']}</p>
                    </div>
                    <div class="price-box"> 
                      <p class="special-price"> <span class="price-label"></span> <span class="price">  $${data[i]['product']['new_price'].toFixed(2)}</span> </p> <p class="old-price"> <span class="price-label"></span> <span class="price">  $${data[i]['product']['price'].toFixed(2)} </span> </p>
                    </div>
                    <div class="actions">
                    <button class="button btn-cart ajx-cart" onclick = "functionAddToBasket($(this).attr('data'))" title="Add to Cart" type="button" data="${data[i]['id']}"><span>Add to Cart</span></button>
                    <span class="add-to-links" onclick = "functionAddToWishlist($(this).attr('data'))" data="${data[i]['id']}"> <button type="button" title="Add to Wishlist" class="button link-wishlist"><span>Add to Wishlist</span></button> </span> </div>
                  </div>
                </li>
                `
            }
            else {
              document.getElementById('products-list').innerHTML += `
                <li class="item first">
                  <div class="product-image"> <a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
                  <div class="product-shop">
                    <h2 class="product-name"><a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                    <div class="desc std">
                      <p>${data[i]['product']['overview']}</p>
                    </div>
                    <div class="price-box"> 
                      <p class="special-price"> <span class="price-label"></span> <span class="price"> $${data[i]['product']['price'].toFixed(2)}</span> </p>
                    </div>
                    <div class="actions">
                    <button class="button btn-cart ajx-cart" onclick = "functionAddToBasket($(this).attr('data'))" title="Add to Cart" type="button" data="${data[i]['id']}"><span>Add to Cart</span></button>
                    <span class="add-to-links" onclick = "functionAddToWishlist($(this).attr('data'))" data="${data[i]['id']}"> <button type="button" title="Add to Wishlist" class="button link-wishlist"><span>Add to Wishlist</span></button> </span> </div>
                  </div>
                </li>
                `
            }
          }
        }
      }
    })
  }
}

let filterCategory = document.getElementsByClassName('category-field');
for (let i = 0; i < filterCategory.length; i++) {
  filterCategory[i].onclick = function () {
    const categoryId = this.getAttribute('data');
    categoryFilter.filterProduct(categoryId);
  }
}

const manufacturerFilter = {
  url: `${location.origin}/api/product_versions/`,

  filterManufacturerProduct(manufacturerId) {
    let url = this.url;
    if (manufacturerId) {
      url += `?product__manufacturer__name=${manufacturerId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {
        console.log(data[i]);
        if (data[i]['product']['manufacturer']['name'] == manufacturerId) {
          if (data[i]['product']['in_sale'] == true) {
            document.getElementById('products-list').innerHTML += `
              <li class="item first">
                <div class="product-image"> <a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
                <div class="product-shop">
                  <h2 class="product-name"><a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                  <div class="desc std">
                    <p>${data[i]['product']['overview']}</p>
                  </div>
                  <div class="price-box"> 
                    <p class="special-price"> <span class="price-label"></span> <span class="price">  $${data[i]['product']['new_price'].toFixed(2)}</span> </p> <p class="old-price"> <span class="price-label"></span> <span class="price">  $${data[i]['product']['price'].toFixed(2)} </span> </p>
                  </div>
                  <div class="actions">
                  <button class="button btn-cart ajx-cart" onclick = "functionAddToBasket($(this).attr('data'))" title="Add to Cart" type="button" data="${data[i]['id']}"><span>Add to Cart</span></button>
                  <span class="add-to-links" onclick = "functionAddToWishlist($(this).attr('data'))" data="${data[i]['id']}"> <button type="button" title="Add to Wishlist" class="button link-wishlist"><span>Add to Wishlist</span></button> </span> </div>
                </div>
              </li>
              `
          }
          else {
            document.getElementById('products-list').innerHTML += `
              <li class="item first">
                <div class="product-image"> <a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
                <div class="product-shop">
                  <h2 class="product-name"><a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                  <div class="desc std">
                    <p>${data[i]['product']['overview']}</p>
                  </div>
                  <div class="price-box"> 
                    <p class="special-price"> <span class="price-label"></span> <span class="price"> $${data[i]['product']['price'].toFixed(2)}</span> </p>
                  </div>
                  <div class="actions">
                  <button class="button btn-cart ajx-cart" onclick = "functionAddToBasket($(this).attr('data'))" title="Add to Cart" type="button" data="${data[i]['id']}"><span>Add to Cart</span></button>
                  <span class="add-to-links" onclick = "functionAddToWishlist($(this).attr('data'))" data="${data[i]['id']}"> <button type="button" title="Add to Wishlist" class="button link-wishlist"><span>Add to Wishlist</span></button> </span> </div>
                </div>
              </li>
              `
          }
        }
      }
    })
  }
}

let filterManufacturer = document.getElementsByClassName('manufacturer-category');
for (let i = 0; i < filterManufacturer.length; i++) {
  filterManufacturer[i].onclick = function () {
    const ManufacturerId = this.getAttribute('data');
    manufacturerFilter.filterManufacturerProduct(ManufacturerId);
  }
}

const colorFilter = {
  url: `${location.origin}/api/product_versions/`,

  filterColorProduct(ColorId) {
    let url = this.url;
    if (ColorId) {
      url += `?color__name=${ColorId}`;
    }
    fetch(url).then(response => response.json()).then(data => {
      document.getElementById('products-list').innerHTML = ''
      for (let i in data) {console.log(ColorId);
        if (data[i]['color']['name'] == ColorId) {
          if (data[i]['product']['in_sale'] == true) {
            document.getElementById('products-list').innerHTML += `
              <li class="item first">
                <div class="product-image"> <a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
                <div class="product-shop">
                  <h2 class="product-name"><a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                  <div class="desc std">
                    <p>${data[i]['product']['overview']}</p>
                  </div>
                  <div class="price-box"> 
                    <p class="special-price"> <span class="price-label"></span> <span class="price">  $${data[i]['product']['new_price'].toFixed(2)}</span> </p> <p class="old-price"> <span class="price-label"></span> <span class="price">  $${data[i]['product']['price'].toFixed(2)} </span> </p>
                  </div>
                  <div class="actions">
                  <button class="button btn-cart ajx-cart" onclick = "functionAddToBasket($(this).attr('data'))" title="Add to Cart" type="button" data="${data[i]['id']}"><span>Add to Cart</span></button>
                  <span class="add-to-links" onclick = "functionAddToWishlist($(this).attr('data'))" data="${data[i]['id']}"> <button type="button" title="Add to Wishlist" class="button link-wishlist"><span>Add to Wishlist</span></button> </span> </div>
                </div>
              </li>
              `
          }
          else {
            document.getElementById('products-list').innerHTML += `
              <li class="item first">
                <div class="product-image"> <a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense"> <img class="small-image" src="${data[i]['cover_image']}" alt="HTC Rhyme Sense" width="150px" height="325px"> </a> </div>
                <div class="product-shop">
                  <h2 class="product-name"><a href="${data[i]['product']['detail_url']}" title="HTC Rhyme Sense">${data[i]['product']['name']}</a></h2>
                  <div class="desc std">
                    <p>${data[i]['product']['overview']}</p>
                  </div>
                  <div class="price-box"> 
                    <p class="special-price"> <span class="price-label"></span> <span class="price"> $${data[i]['product']['price'].toFixed(2)}</span> </p>
                  </div>
                  <div class="actions">
                  <button class="button btn-cart ajx-cart" onclick = "functionAddToBasket($(this).attr('data'))" title="Add to Cart" type="button" data="${data[i]['id']}"><span>Add to Cart</span></button>
                  <span class="add-to-links" onclick = "functionAddToWishlist($(this).attr('data'))" data="${data[i]['id']}"> <button type="button" title="Add to Wishlist" class="button link-wishlist"><span>Add to Wishlist</span></button> </span> </div>
                </div>
              </li>
              `
          }
        }
      }
    })
  }
}

let filterColor = document.getElementsByClassName('color-category');
for (let i = 0; i < filterColor.length; i++) {
  filterColor[i].onclick = function () {
    const ColorId = this.getAttribute('data');
    colorFilter.filterColorProduct(ColorId);
  }
}
