from argparse import ArgumentParser, _SubParsersAction
from Enhancer \
    import (optimize_all_user, optimize_user, optimize_category_image,
            optimize_image, StateHolder)


def all_user(args):
    optimize_all_user()


def user(args):
    optimize_user(args.user_name, StateHolder())


def category(args):
    optimize_category_image(args.user_name, args.category_name, StateHolder())


def image(args):
    optimize_image(args.user_name, args.category_name,
                   args.image_path, StateHolder())


if __name__ == "__main__":
    # コマンドラインパーサーを作成
    parser = ArgumentParser(description='manual optimize')
    subparsers = parser.add_subparsers()

    parser_all = subparsers.add_parser('all_user', help='see `all_user -h`')
    parser_all.set_defaults(handler=all_user)

    parser_user = subparsers.add_parser('user', help='see `user -h`')
    parser_user.add_argument('-u', '--user_name', required=True)
    parser_user.set_defaults(handler=user)

    parser_category = \
        subparsers.add_parser('category', help='see `category -h`')
    parser_category.add_argument('-u', '--user_name', required=True)
    parser_category.add_argument('-c', '--category_name', required=True)
    parser_category.set_defaults(handler=category)

    parser_image = \
        subparsers.add_parser('image', help='see `image -h`')
    parser_image.add_argument('-u', '--user_name', required=True)
    parser_image.add_argument('-c', '--category_name', required=True)
    parser_image.add_argument('-i', '--image_path', required=True)
    parser_image.set_defaults(handler=image)
    
    # コマンドライン引数をパースして対応するハンドラ関数を実行
    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        # 未知のサブコマンドの場合はヘルプを表示
        parser.print_help()
