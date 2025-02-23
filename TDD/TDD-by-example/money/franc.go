package money

type Franc struct {
	amount int
}

func (f *Franc) Times(multiplier int) *Franc {
	return &Franc{amount: f.amount * multiplier}
}
func (f *Franc) Equals(other any) bool {
	otherFranc, ok := other.(*Franc)
	return ok && f.amount == otherFranc.amount
}
func NewFranc(amount int) *Franc {
	return &Franc{amount: amount}
}
