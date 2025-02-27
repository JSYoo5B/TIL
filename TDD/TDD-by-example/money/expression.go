package money

type Expression interface {
	Reduce(bank *Bank, to string) Money
}

type Sum struct {
	Augend Money
	Addend Money
}

func (s *Sum) Reduce(bank *Bank, to string) Money {
	amount := s.Augend.Reduce(bank, to).getAmount() +
		s.Addend.Reduce(bank, to).getAmount()
	return newMoney(amount, to)
}

func NewSum(augend, addend Money) *Sum {
	return &Sum{
		Augend: augend,
		Addend: addend,
	}
}
