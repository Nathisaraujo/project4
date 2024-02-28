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
      console.log("chegou nessa bosta")
      // Handle success, e.g., update UI or show a message
      const responseData = await fetch(postUrl, {
        method: "POST",
        body: formData,
      });
      // const postSlug = responseData.post_slug;
      // const postSlug = likeForm.querySelector('[name="post_id"]').value;
      const likeCount = responseData.like_count;
      console.log("chegou nessa bosta2")
      const likeCounter = document.querySelector(`.likeCounter[data-post-slug="${postUrl}"]`);
      console.log("chegou nessa bosta3")
      if (likeCounter) {
        likeCounter.innerText = likeCount;
        console.log("Post liked successfully");
      } else {
        console.error('Like counter element not found');
      }
    
    } else {
      // Handle error response
      console.error("Failed to like post");
    }
  } catch (error) {
    console.error("Error:", error);
    console.log("bosta")
  }
});