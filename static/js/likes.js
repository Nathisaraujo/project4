// const likeButtons = document.querySelectorAll('.btn-like');
// const likeForm = document.getElementById("likeForm");

// likeForm.addEventListener("submit", async (e) => {
//   e.preventDefault();
//   const formData = new FormData(likeForm);
//   try {
//     const response = await fetch(likeForm.action, {
//       method: "POST",
//       body: formData,
//     });
//     console.log("chegou nessa bosta4")
//     if (response.ok) {
//       console.log("chegou nessa bosta")
//       const responseData = await response.json();
//       const likeCount = responseData.like_count;
//       console.log("chegou nessa bosta2")
//       const postSlug = likeForm.getAttribute('data-post-slug');
//       const likeCounter = document.querySelector(`.likeCounter[data-post-slug="${postUrl}"]`);
//       console.log("chegou nessa bosta3")
//       if (likeCounter) {
//         likeCounter.innerText = likeCount;
//         console.log("Post liked successfully");
//       } else {
//         console.error('Like counter element not found');
//       }
//     } else {
//       console.error("Failed to like post");
//     }
//   } catch (error) {
//     console.error("Error:", error);
//     console.log("bosta")
//   }
// });