while True:
    ask_user = input("Как дела?")
    if ask_user == 'Хорошо':
    
        break
    else:
        print('Как дела?')

    except KeyboardInterrupt:
        print("Пока")
        break 
#2
def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

        except ZeroDivisionError:
            print("Деление на ноль невозможно")
        except SyntaxError:
            print("Введите, пожалуйста, коректное выыражение")
        except OSError:
            print("Извините, системная ошибка")