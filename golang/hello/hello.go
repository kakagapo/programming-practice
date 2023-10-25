package main

// Importing mutiple packages
import (
	"fmt"

	"github.com/google/uuid" // you can also import from github directly like below
	"rsc.io/quote"
)

// alt format to import one item at a time like
// import "fmt"

func main() {

	// simple string print
	fmt.Println("Hello world!!!")

	// invoking a simple function
	fmt.Println(quote.Go())

	for i := 0; i < 5; i++ {
		// using built-in function and not the one from fmt package
		println(uuid.New().String())
	}
}
