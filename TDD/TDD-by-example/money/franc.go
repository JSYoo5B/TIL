package money

type Franc struct {
	money
}

func NewFranc(amount int) *Franc {
	return &Franc{
		money: *newMoney(amount, "CHF"),
	}
}
