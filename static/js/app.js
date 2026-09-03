// Initialize Lucide Icons
lucide.createIcons();

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("search-form");
    const input = document.getElementById("movie-input");
    const loader = document.getElementById("loader");
    const resultContainer = document.getElementById("result-container");
    const tags = document.querySelectorAll(".tag");

    // UI Elements for mapping
    const elTitle = document.getElementById("res-title");
    const elYear = document.getElementById("res-year");
    const elRating = document.getElementById("res-rating");
    const elDirector = document.getElementById("res-director");
    const elGenres = document.getElementById("res-genres");
    const elCast = document.getElementById("res-cast");
    const elSummary = document.getElementById("res-summary");
    const elJson = document.getElementById("res-json");

    let currentMovieData = null;

    // Quick tag clicks
    tags.forEach(tag => {
        tag.addEventListener("click", () => {
            input.value = tag.innerText;
            form.dispatchEvent(new Event("submit"));
        });
    });

    // Form submission
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        
        const movieName = input.value.trim();
        if (!movieName) {
            showToast("Please enter a movie name.", "error");
            return;
        }

        // UI Reset & Loading state
        resultContainer.classList.add("hidden");
        loader.classList.remove("hidden");

        try {
            const response = await fetch("/api/mine", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ movie_name: movieName })
            });

            if (!response.ok) {
                throw new Error("Failed to mine movie details");
            }

            const data = await response.json();
            currentMovieData = data;
            
            renderData(data);

            // Show results
            loader.classList.add("hidden");
            resultContainer.classList.remove("hidden");
            
            // Scroll to results
            resultContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });

        } catch (error) {
            loader.classList.add("hidden");
            showToast(error.message || "An error occurred", "error");
        }
    });

    function renderData(data) {
        // Metrics
        elTitle.textContent = data.title;
        elYear.textContent = data.release_year || "N/A";
        elRating.textContent = data.rating ? `${data.rating}/10` : "N/A";
        elDirector.textContent = data.director || "N/A";
        elSummary.textContent = data.summary;

        // Genres
        elGenres.innerHTML = "";
        if (data.genre && data.genre.length > 0) {
            data.genre.forEach(g => {
                const span = document.createElement("span");
                span.className = "badge";
                span.textContent = g;
                elGenres.appendChild(span);
            });
        } else {
            elGenres.textContent = "N/A";
        }

        // Cast
        elCast.innerHTML = "";
        if (data.cast && data.cast.length > 0) {
            data.cast.forEach(actor => {
                const li = document.createElement("li");
                li.textContent = actor;
                elCast.appendChild(li);
            });
        } else {
            elCast.textContent = "N/A";
        }

        // JSON string formatting
        elJson.textContent = JSON.stringify(data, null, 4);
    }

    // JSON Actions
    document.getElementById("copy-json-btn").addEventListener("click", () => {
        if (currentMovieData) {
            navigator.clipboard.writeText(JSON.stringify(currentMovieData, null, 4))
                .then(() => showToast("JSON copied to clipboard!"))
                .catch(() => showToast("Failed to copy", "error"));
        }
    });

    document.getElementById("download-json-btn").addEventListener("click", () => {
        if (!currentMovieData) return;
        
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(currentMovieData, null, 4));
        const a = document.createElement('a');
        const safeTitle = currentMovieData.title.replace(/[^a-z0-9]/gi, '_').toLowerCase();
        
        a.setAttribute("href", dataStr);
        a.setAttribute("download", `${safeTitle}_data.json`);
        document.body.appendChild(a);
        a.click();
        a.remove();
    });

    // Toast Notification System
    function showToast(message, type = "success") {
        const toast = document.getElementById("toast");
        const msg = document.getElementById("toast-msg");
        const icon = document.getElementById("toast-icon");
        
        msg.textContent = message;
        
        if (type === "error") {
            toast.classList.add("error");
            icon.setAttribute("data-lucide", "alert-circle");
        } else {
            toast.classList.remove("error");
            icon.setAttribute("data-lucide", "check-circle");
        }
        
        lucide.createIcons(); // re-render icon
        
        toast.classList.add("show");
        
        setTimeout(() => {
            toast.classList.remove("show");
        }, 3000);
    }
});
