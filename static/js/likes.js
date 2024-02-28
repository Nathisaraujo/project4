const likeForms = document.querySelectorAll("likeForm");
const likeCountElement = document.getElementById("likeCount");


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
        likeCountElement.textContent = responseData.likes_count;
        console.log("Post liked successfully");
      } else {
        // Handle error response
        console.error("Failed to like post");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  });