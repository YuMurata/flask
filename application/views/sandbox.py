from flask import Blueprint, render_template, request
from application.services.compare_image import image_path_dict, EnhanceEncoder
from application.services.compare_image import ImageEnhancer, CompareSession
from application.services.compare_image.Tournament import Tournament
from application.models import CompareData, ScoredParam, User, Unko
from application.database import db
from flask_login import login_required

sandbox_bp = Blueprint('sandbox_bp', __name__)


@sandbox_bp.route('/sandbox')
def index():
    return '''  
    <ul>  
        <li><a href="/sandbox_1">data</a></li>
        <li><a href="/sandbox_3">comparer</a></li>
        <li><a href="/sandbox_4">add_compare_data</a></li>
        <li><a href="/sandbox_5">save_param</a></li>
    </ul>

    '''


@sandbox_bp.route('/sandbox_1')
def data():
    image_dict_list = [
        {
            'path': 'static/images/'+image_path.name,
            'name': name,
            'is_compared': True
        }
        for name, image_path in image_path_dict.items()
    ]
    image_dict_list[0]['is_compared'] = False
    n = 4
    image_dict_table = [image_dict_list[idx:idx+n]
                        for idx in range(0, len(image_dict_list), n)]

    return render_template('image/data.html', image_dict_table=image_dict_table)


@sandbox_bp.route('/sandbox_2', methods=['POST'])
def scored_param():
    image_name = request.form['select']

    image_path = image_path_dict[image_name]
    encoder = EnhanceEncoder(image_path)
    param_list = ImageEnhancer.generate_random_param_list(14)

    image_list = [encoder.Encode(param) for param in param_list]

    return render_template('image/scored_param.html', image_list=image_list)


@sandbox_bp.route('/sandbox_3')
@login_required
def comparer():
    image_name = 'flower'

    if not CompareSession.is_in_session():
        CompareSession.add(image_name)

    comparer = CompareSession.get()
    count = comparer.tournament.get_match_num
    is_complete, (left_player, right_player) = comparer.tournament.new_match()
    CompareSession.commit()

    return render_template('image/compare.html',
                           left_image=left_player.decode(),
                           right_image=right_player.decode(),
                           count=count)


def add_user():
    user = User('unko', 'tinko', '1')

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        raise Exception('user commit failure :(')
    finally:
        db.session.close()


@sandbox_bp.route('/sandbox_4')
def add_compare_data():
    player_num = 100

    ret = 'commit success :)'

    user = User.query.first()
    if user is None:
        try:
            add_user()
        except Exception as e:
            return e

        user = User.query.first()

    compare_data_list = [CompareData(user, param)
                         for param in ImageEnhancer.generate_random_param_list(player_num)]
    compare_data = compare_data_list[0]

    try:
        db.session.add(compare_data)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        ret = 'commit failure :('
    finally:
        db.session.close()

    return f'''
        <div>{ret}</div>
        <a href="/sandbox_4">once more</a>
    '''


@sandbox_bp.route('/sandbox_5')
def save_param():
    user = User.query.first()
    if user is None:
        try:
            add_user()
        except Exception as e:
            return e

        user = User.query.first()
    print(user)
    new_param = ScoredParam(user, 'comparer.image_name')

    ret = 'commit success :)'

    try:
        db.session.add(new_param)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        ret = 'commit failure :('
    finally:
        db.session.close()
    return f'''
        <div>{ret}</div>
        <a href="/sandbox_5">once more</a>
    '''


class AhoPlayer(Tournament.Player):
    def __init__(self, param):
        super().__init__(param)

    def decode(self):
        return self.param


@sandbox_bp.route('/sandbox_6')
def pickle_tournament():
    player_num = 100

    player_list = [AhoPlayer(param)
                   for param in ImageEnhancer.generate_random_param_list(player_num)]
    tournament = Tournament.Tournament(player_list)

    unko = Unko(kuso=tournament)

    try:
        db.session.add(unko)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
        return 'commit failure :('
    finally:
        db.session.close()

    def buri() -> Tournament.Tournament:
        return Unko.query.first().kuso

    kuso = buri()

    return f'''
        <div>{kuso.current_player_index_list}</div>
        <div>{tournament.current_player_index_list}</div>
        <a href="/sandbox_6">once more</a>
    '''
    return pickle.dumps(tournament)
