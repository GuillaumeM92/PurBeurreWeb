function autocomplete(input, list) {
  /* propose autocompleted product names when the user starts typing in the search bar */
  let list_length = 0
  /* list_length is used to ensure the autocomplete list is not longer than 5 products */

  input.addEventListener("input", function (e) {
    var newDiv, newRow, index, userInput = this.value;
    closeAllLists(input);
    if (!userInput) { return false; }

    /* create a DIV element that will contain the product names */
    newDiv = document.createElement("DIV");
    newDiv.setAttribute("id", this.id + "autocomplete-list");
    newDiv.setAttribute("class", "autocomplete-items");
    this.parentNode.appendChild(newDiv);

    for (index = 0; index < list.length; index++) {
      /* compare the input string with all product names */
      if (list[index].substr(0, userInput.length).toUpperCase() == userInput.toUpperCase()) {
        if (list_length < 5) {
          /* create and fill a new row for the first 5 matching product names */
          newRow = document.createElement("DIV");
          list_length += 1;
          qsd = "<strong>" + list[index].substr(0, userInput.length) + "</strong>";
          // cqsd = fromWindows1252(qsd)
          newRow.innerHTML = qsd;
          qsd2 = list[index].substr(userInput.length);
          // cqsd2 = fromWindows1252(qsd2)
          newRow.innerHTML += qsd2;
          newRow.innerHTML += "<input type='hidden' value='" + list[index] + "'>";
          newRow.addEventListener("click", function (e) {
            input.value = this.getElementsByTagName("input")[0].value;
            closeAllLists(input);
          });
          newDiv.appendChild(newRow);
        }
      }
    }
    list_length = 0;
  });
};

function closeAllLists(element, input) {
  /*close all autocomplete lists in the document, except the one passed as an argument:*/
  var autoCompletetItems = document.getElementsByClassName("autocomplete-items");
  for (var index = 0; index < autoCompletetItems.length; index++) {
    if (element != autoCompletetItems[index] && element != input) {
      autoCompletetItems[index].parentNode.removeChild(autoCompletetItems[index]);
    }
  }
}

/*initiate the autocomplete function, using the product names list as possible autocomplete values:*/
if (document.getElementById("search-top")) {
  autocomplete(document.getElementById("search-top"), products);
}
if (document.getElementById("search-middle")) {
  autocomplete(document.getElementById("search-middle"), products);
}
