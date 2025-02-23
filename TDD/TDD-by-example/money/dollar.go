package money

type Dollar struct {
	money
}

func NewDollar(amount int) *Dollar {
	return &Dollar{
		money: *newMoney(amount, "USD"),
	}
}
