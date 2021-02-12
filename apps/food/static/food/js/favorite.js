// jquery ajax call to add a product to the user favorites
$(".favorite-button").on("click", function (error) {
    error.preventDefault();

    let searched_product_id = this.getAttribute("productID");
    let substitute_id = this.value;
    let is_authenticated = this.getAttribute("isAuthenticated");
    let email = this.getAttribute("user");
    let status = this.getAttribute("name");

    if (is_authenticated == "True") {

        $.ajax({
            data: { searched_product_id, substitute_id, is_authenticated, email, status },
            type: $(this).attr("method"), // GET or POST
            url: "/favorite",
            success: function (response) { },
            error: function (response) {
                alert("an error occured");
            }
        });

        if (status == "add-favorite") {
            this.innerHTML = "<span style='color:teal; margin:5px'> Produit ajouté aux favoris ! </span>";
        } else {
            this.innerHTML = "<span style='color:teal; margin:5px'> Produit retiré des favoris ! </span>";
        }
    }

    else {
        console.log("user is not authenticated")
        this.innerHTML = "<span> Vous devez être connecté pour ajouter un produit aux favoris ! </span>";
    }
});
