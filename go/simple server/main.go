package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

// request body struct
type ResponseBody struct {
	OK      bool   `json:"ok"`
	Message string `json:"message"`
	Data    any    `json:"data"`
}

// response body struct
type Request struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

// testing middleware
func middlwareCheck(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		log.Println("Before handler,,,,,,")

		next.ServeHTTP(w, r)
	})
}

// logging middleware
func logMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		log := fmt.Sprintf("|%s |%v |%s", r.Method, r.URL, r.UserAgent())
		fmt.Println(log)

		next.ServeHTTP(w, r)
	})
}

// main func
func main() {
	//serving the css file
	fs := http.FileServer(http.Dir("./styles"))
	http.Handle("/styles/", http.StripPrefix("/styles/", fs))

	//user controller
	http.HandleFunc("/user", func(w http.ResponseWriter, r *http.Request) {
		method := r.Method
		if method != http.MethodPost {
			w.WriteHeader(http.StatusMethodNotAllowed)
			response := ResponseBody{
				OK:      false,
				Message: "invalid method",
			}

			if err := json.NewEncoder(w).Encode(response); err != nil {
				w.WriteHeader(http.StatusInternalServerError)
			}

			return
		}

		var reqBody Request

		if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
			w.WriteHeader(http.StatusBadRequest)
			return
		}

		w.WriteHeader(http.StatusOK)
		response := ResponseBody{
			OK:      true,
			Message: "correct",
			Data:    reqBody,
		}
		json.NewEncoder(w).Encode(response)
	})

	//testing with middleware
	http.Handle("/middleware", middlwareCheck(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		response := ResponseBody{
			OK:      true,
			Message: "testing middleware",
		}
		json.NewEncoder(w).Encode(response)
	})))

	//testing the log middleware
	http.Handle("/log", logMiddleware(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		response := ResponseBody{
			OK:      true,
			Message: "testing log middleware",
		}
		json.NewEncoder(w).Encode(response)
	})))

	//home controller
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		//reading the file for the root dir
		content, err := os.ReadFile("index.html")
		if err != nil {
			return
		}

		//sending the status 200, content-type, text/html and the html it self
		w.WriteHeader(http.StatusOK)
		w.Header().Set("Content-Type", "text/html")
		w.Write(content)
	})

	//server starting point
	fmt.Println("server is running on http://localhost:8080/")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println(err)
	}
}
