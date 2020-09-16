const cart_count_element = document.getElementById('cart_count');

function addToCart(obj, newProductId, newProdPrice, newProdName, newProdUserId) {
   var cookies = document.cookie.split('=');
   var product_cookie = cookies[1];
   var exist=false;
   var newProd = newProductId + ":" + newProdPrice + ":" + newProdName + ":" + newProdUserId;

    if(product_cookie){
      var products_saved = product_cookie.split('-');
      for( i = 0; i < products_saved.length; i++){
            if(products_saved[i] == newProd){
                exist = true;
                break;
            }
      }
      if(!exist){
        var newCookie = "products=" + product_cookie + "-" + newProd;
        document.cookie = newCookie;
        cart_count_element.innerHTML = ""+(products_saved.length+1);
      }
    }else{
      document.cookie = "products="+newProd;
      cart_count_element.innerHTML = ""+(products_saved.length);
    }

}

const cart_session = document.getElementById('cart_prod_session');
const totalPrice = document.getElementById('totalPrice');
const checkout_page_cart = document.getElementById('checkout_cart');
const totalOrder = document.getElementById('totalOrder');

function removeItem(productId){
   var cookies = document.cookie.split('=');
   var product_cookie = cookies[1];

    if(product_cookie){
      var newProd = "";
      var products_saved = product_cookie.split('-');
      for( i = 0; i < products_saved.length; i++){
        var id = products_saved[i].split(':')[0]
         if(id != productId){
             newProd += (newProd != "")? "-" + products_saved[i] : products_saved[i];
         }
      }
      var newCookie = "products=" + newProd;
      document.cookie = newCookie;
      fillCart();
      if(checkout_page_cart){
          fillCheckoutPageCart()
      }
    }
}

function addElementsToCart(product_list, element_to_print){
    var totalprice = 0.00;
    var cart_count = 0;
    var innerHTML = "";
    try{
        for(i = 0; i < product_list.length; i++){
                var info = product_list[i].split(":");
                var id = info[0];
                var price = info[1];
                var name = info[2];
                var user_id = info[3];
                totalprice += Number(price);
                innerHTML += "<div id='"+id+"' class='shp__single__product'><div class='shp__pro__thumb'><a href='/product-details'><img src='static/users/"+user_id+"/"+id+".jpg' alt='product images'></a></div><div class='shp__pro__details'><h2><a href='/product-details'>"+name+"</a></h2><span class='quantity'>QTY: 1</span><span class='shp__price'>€"+price+"</span></div><div class='remove__btn'><a onClick=removeItem('"+id+"') title='Remove this item'><i class='zmdi zmdi-close'></i></a></div></div>";
                cart_count += 1;
        }
    }catch(err){ }
    element_to_print.innerHTML = innerHTML;
    totalPrice.innerHTML = "€"+totalprice;
    if(totalOrder){
        totalOrder.innerHTML = "€"+totalprice;
    }
    if(cart_count_element){
        cart_count_element.innerHTML = cart_count;
    }
}

function removeChilds(element){
    while (element.hasChildNodes()) {
      element.removeChild(element.firstChild);
    }
}

function fillCheckoutCarts(checkout_cart_element){
    removeChilds(checkout_cart_element);
    var cookies = document.cookie.split('=');
    var product_cookie = cookies[1];

    if(product_cookie){
        var list_Of_Products = product_cookie.split('-');
    }else{
        var text = document.createElement("p");
        text.innerHTML = "No products selected!";
        checkout_cart_element.appendChild(text);
    }
    addElementsToCart(list_Of_Products, checkout_cart_element);
}

function fillCart(){
    fillCheckoutCarts(cart_session);
}

function fillCheckoutPageCart(){
    fillCheckoutCarts(checkout_page_cart);
}


if(checkout_page_cart){
    fillCheckoutPageCart()
}

var cookies = document.cookie.split('=');
var product_cookie = cookies[1];
if(product_cookie){
  var products_saved = product_cookie.split('-');
  cart_count_element.innerHTML = ""+(products_saved.length);
}