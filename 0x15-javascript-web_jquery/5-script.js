$(document).ready(function () {
  // Attach a click event listener to the div with id 'add_item'
  $("#add_item").click(function () {
    // Create a new <li> element with the content "Item"
    var newItem = $("<li>").text("Item");

    // Append the new <li> element to the <ul> with class 'my_list'
    $("ul.my_list").append(newItem);
  });
});

