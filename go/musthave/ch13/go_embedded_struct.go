package main

import (
	"fmt"
	"time"
)

type User struct {
	Name	string
	Id 		int
	Age		int
}

type VipUser struct {
	User
	Level		int
	Since		time.Time
}

func main() {
	var john User = User{"John Doe", 1, 30}
	var johnVip VipUser = VipUser{User: john, Level: 1}
	janeVip := VipUser{User{"Jane Doe", 2, 32}, 2, time.Now()}

	fmt.Println(johnVip)
	fmt.Println(janeVip)

	fmt.Printf("VIP user %s became VIP since %v", janeVip.Name, janeVip.Since)
}
