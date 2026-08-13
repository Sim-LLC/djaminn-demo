export default function ApiService() {
  // const baseURL = "https://musicbrainz.org/ws/2/artist";
  const baseURL = "http://localhost:8000"

  async function request(endpoint, options = {}) {
    const url = `${baseURL}/search?q=${encodeURIComponent(endpoint)}&limit=3`;

    const defaultOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    };

    try {
      const response = await fetch(url, {
        ...defaultOptions,
        ...options,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      throw new Error(`API request failed: ${error.message}`);
    }
  }

  async function get(endpoint) {
    return request(endpoint);
  }

  return {
    get,
  };
}
