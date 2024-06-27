
$(document).ready(function() {
    const editButtons = $(".edit-btn");
    const reviewText = $("#content");
    const reviewForm = $("#reviewForm");
    const submitButton = $("#submitButton");
    const reviewHeading = $("#reviewHeading");

    const deleteModal = new bootstrap.Modal($("#deleteModal"));
    const productDeleteButtons = $(".delete-product");
    const deleteConfirm = $("#deleteConfirm");
    const deleteModalText = $("#deleteModalText");
    const deleteModalLabel = $("#deleteModalLabel");

    editButtons.on('click', function(e) {
        const reviewId = $(this).data("review-id");
        const reviewContent = $("#" + "review" + reviewId).text();
        reviewText.val(reviewContent);
        submitButton.text("Update");
        reviewHeading.text("Edit your review");
        console.log("test")
        console.log(reviewId)
        reviewForm.attr("action", "edit_product_review/" + reviewId);
    });

    productDeleteButtons.on('click', function(e) {
        const productId = $(this).data("product-id");
        deleteModalLabel.text("Delete Product?");
        deleteModalText.text("Are you sure you want to delete this product? This action cannot be undone!");
        deleteConfirm.attr("href", "/products/delete_product/" + productId);
        deleteModal.show();
    });
});