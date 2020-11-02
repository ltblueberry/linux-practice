package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "practice webserver")
	})

	portString := ":8181"
	if port := os.Getenv("PORT"); port != "" {
		portString = fmt.Sprintf(":%s", port)
	}
	http.ListenAndServe(portString, nil)
}
