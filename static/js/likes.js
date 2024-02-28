const likeButtons = document.querySelectorAll('.btn-like');

likeForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData(likeForm);
  try {
    const response = await fetch(postUrl, {
      method: "POST",
      body: formData,
    });
    if (response.ok) {
      // Handle success, e.g., update UI or show a message
      
      console.log("Post liked successfully");
    } else {
      // Handle error response
      console.error("Failed to like post");
    }
  } catch (error) {
    console.error("Error:", error);
  }
});