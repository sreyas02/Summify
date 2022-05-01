// Future JavaScript will go here

var requestOptions = {
  method: "GET",
  redirect: "follow",
  mode: "no-cors"
};

chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
  // gets the current tab that the user is on
  var url = tabs[0].url;
  // document.getElementById("url").innerHTML = url;
  // displays it to the user

  // API call
  fetch("http://127.0.0.1:5000/query?article=" + url)
    .then((response) => response.json())
    .then(
      (result) =>
        (document.getElementById("summary").innerHTML = result.summary)
    )
    .catch((error) => console.trace(error));
});


